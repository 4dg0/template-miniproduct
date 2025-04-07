from pydantic import BaseModel


class CreateStripeCustomer(BaseModel):
    pbUserId: str
    email: str
    name: str = ""
    phone: str | None = None
    address: dict[str, str] | None = None
    metadata: dict[str, str] | None = None


class CreateStripeCheckoutSession(BaseModel):
    customerId: str
    lookupKey: str


class CreateStripePortalSession(BaseModel):
    customerId: str
    currentUrl: str
