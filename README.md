# Account Management API
Your task is to build a service capable of processing account management operations via a REST API.\
Here's what you should pay attention to:
1. **Acceptance Criteria** define what should be done.
2. **Core Skills** define which skills you're expected to demonstrate.
3. Feel free to re-structure the code. However, one requirement is that the service must run on localhost:8080.

## Acceptance Criteria
- All contract tests pass.
- The service amends account balance with the `/amount` endpoint.
- The service returns the current account balance with the `/balance` endpoint.
- The service supports safe request retries.

## Core Skills
- Git
- REST API
- System design
- Code quality
- Test driven development
- Data structures
- Concurrency
- Idempotency

## Before you start
### Setting up the project
Follow [server-setup.md](server-setup.md).

### Running contract tests
- Make sure [Newman](https://learning.getpostman.com/docs/postman/collection_runs/command_line_integration_with_newman/) is installed.
- Access the test spec [here](https://documenter.getpostman.com/view/9217291/SVzz2yeW).
- Run `newman run https://www.getpostman.com/collections/e25cb1e0b23342ca49d6`.

---
Delivered with ❤️ by [coreskills.dev](https://coreskills.dev)