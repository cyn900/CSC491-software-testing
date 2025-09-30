Here’s a clean, student-friendly README section you can drop in under **exercise3_e2e_streamlit**.

---

## 🔍 E2E UI tests with Cypress (Streamlit)

### Prerequisites

* **Python** (same version as the rest of the repo) and `streamlit` installed in your venv
* **Node.js** (comes with `npm`)

### 1) Change into the Streamlit E2E folder

```bash
cd exercise3_e2e_streamlit
```

### 2) Install dependencies

```bash
# Node deps (Cypress + helper to start server and run tests)
npm install
# Optional: Testing Library commands (findByRole, etc.)
npm i -D @testing-library/cypress
```

> If you use `@testing-library/cypress`, enable it by creating `cypress/support/e2e.js` with:
>
> ```js
> import '@testing-library/cypress/add-commands';
> ```
>
> and make sure your `cypress.config.js` **does not** set `supportFile: false`.

### 3) Run the tests

**Headless (CI-style):**

```bash
npm run test:e2e
```

**Watch the UI (headed):**

```bash
# Terminal 1 – start the Streamlit app
npm run start:streamlit

# Terminal 2 – open Cypress runner (pick Chrome or Electron)
npm run cy:open
```