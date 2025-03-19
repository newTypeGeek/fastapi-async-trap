# fastapi-async-trap

- We use FastAPI to demonstrate misuse of async functions in router level
- When an async endpoint `/fake-async` involves a sync function call , it would block the event loop
- Hence, when you try to call `/health-check` endpoint, it is blocked

- On the other hand, if you call `/real-async` which involves async function call, it does not block event loop. Therefore, `/health-check` can be succesfully called
