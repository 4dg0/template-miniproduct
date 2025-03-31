import { z } from 'zod';

export const UserSchema = z.object({
	id: z.string(),
	name: z.string(),
	email: z.string().email().optional(),
	avatar: z.string().optional(),
	credits: z.number(),
	verified: z.boolean(),
	created: z.string(),
	updated: z.string()
});
