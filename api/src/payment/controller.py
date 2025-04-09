# payment_router.py
import stripe
from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from src.config import pb, env, get_logger

from .models import *

logger = get_logger(__name__)

payment_router = APIRouter(prefix="/payment", tags=["payment"])


@payment_router.post("/stripe/customers")
async def create_stripe_customer(dto: CreateStripeCustomer) -> JSONResponse:
    customers = stripe.Customer.list(email=dto.email).data
    customer = customers[0] if len(customers) > 0 else None

    if not customer:
        logger.info("Creating new Stripe customer", extra={"payload": dto.model_dump()})
        customer = stripe.Customer.create(
            name=dto.name,
            email=dto.email,
            metadata=dto.metadata,
        )
        await pb.collection("users").update(
            dto.pbUserId, {"stripe_customer": customer.id}
        )
    return JSONResponse({"id": customer.id})


@payment_router.post("/stripe/create-checkout-session")
async def create_checkout_session(dto: CreateStripeCheckoutSession) -> JSONResponse:
    prices = stripe.Price.list(lookup_keys=[dto.lookupKey], expand=["data.product"])

    if not prices.data:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Invalid lookup key: no prices found"},
        )

    checkout_session = stripe.checkout.Session.create(
        customer=dto.customerId,
        line_items=[
            {
                "price": prices.data[0].id,
            },
        ],
        mode="subscription",
        success_url=f"{env.web_url}/?success=true",
        cancel_url=f"{env.web_url}/?cancel=true",
    )
    return JSONResponse(content={"sessionId": checkout_session.id})


@payment_router.post("/stripe/create-portal-session")
async def create_portal_session(dto: CreateStripePortalSession):
    session = stripe.billing_portal.Session.create(
        customer=dto.customerId,
        return_url=dto.currentUrl,
    )
    return JSONResponse(content={"url": session.url})


@payment_router.post("/stripe/webhook")
async def stripe_webhook(request: Request):
    body = await request.body()

    signature = request.headers.get("stripe-signature")
    event = stripe.Webhook.construct_event(
        payload=body,
        sig_header=signature,
        secret=env.stripe_webhook_secret,
    )
    data = event["data"]
    event_type = event["type"]
    data_object = data["object"]

    logger.info(f"event {event_type} {data_object}")

    if event_type == "checkout.session.completed":
        ...
    # elif event_type == "customer.subscription.trial_will_end":
    # print("Subscription trial will end")
    # elif event_type == "customer.subscription.created":
    #     print("Subscription created %s", event.id)
    elif event_type == "customer.subscription.updated":
        ...
    elif event_type == "customer.subscription.deleted":
        ...
    elif event_type == "entitlements.active_entitlement_summary.updated":
        ...
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "success"})
