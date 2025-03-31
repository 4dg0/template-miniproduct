import { z } from 'zod';
import { pb } from '$lib/config/pb';
import { UserSchema } from '$lib/models/user';

// REACTIVE PROVIDER CLASS
class UserProvider {
	user: z.infer<typeof UserSchema> | null = $state(null);

	set(user: z.infer<typeof UserSchema> | null) {
		this.user = user;
	}
}

export const userProvider = new UserProvider();

// SSE REACTIVE FLOW
export async function subscribeUser() {
	await unsubscribeUser();

	console.log('Subscribing to user', pb.authStore.record?.id);
	if (!pb.authStore.record) return;

	userProvider.set(UserSchema.parse(pb.authStore.record));

	pb.collection('users').subscribe(pb.authStore.record.id, async (e) => {
		console.log('Event user recieved:', e);

		console.log('BEFORE', pb.authStore.record);
		const authResponse = await pb.collection('users').authRefresh();
		pb.authStore.save(authResponse.token, authResponse.record);
		userProvider.set(UserSchema.parse(pb.authStore.record));
		console.log('AFTER', pb.authStore.record);
	});
}

export async function unsubscribeUser() {
	console.log('Unsubscribing from user: ', pb.authStore.record?.id);
	userProvider.set(null);

	if (!pb.authStore.record) return;
	await pb.collection('users').unsubscribe(pb.authStore.record.id);
}
