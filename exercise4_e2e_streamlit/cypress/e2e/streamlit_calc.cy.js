// cypress/support/commands.js (or inline in your spec)
// Open the selectbox labeled "Operation" and choose an option by visible text.
function selectFromStreamlitSelectbox(labelText, optionText) {
  // 1) Find the specific selectbox by its label
  cy.contains(
    '[data-testid="stSelectbox"] [data-testid="stWidgetLabel"] p',
    new RegExp(`^${labelText}$`, 'i')
  )
    .closest('[data-testid="stSelectbox"]')
    .as('box');

  // 2) Open the combobox
  cy.get('@box').find('[role="combobox"]').click({ force: true });

  // 3) Pick the option from the virtual dropdown
  cy.get('ul[data-testid="stSelectboxVirtualDropdown"]', { timeout: 10000 })
    .should('be.visible')
    .within(() => {
      cy.get('li[role="option"]')
        .contains(new RegExp(`^${optionText}$`, 'i'))
        .click({ force: true });
    });

  // 4) (Optional) verify it closed
  cy.get('@box').find('[role="combobox"]').should('have.attr', 'aria-expanded', 'false');
}


// cypress/e2e/streamlit_calc.cy.js
describe('Streamlit Tiny Calculator', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.contains('Tiny Calculator', { timeout: 15000 }).should('exist');
  });

  function setNum(label, value) {
    // Find the number input by its label text near stNumberInput
    cy.contains('[data-testid="stNumberInput"] label p', new RegExp(`^${label}$`, 'i'))
      .closest('[data-testid="stNumberInput"]')
      .find('input[type="number"]')
      .clear()
      .type(String(value), { delay: 0 });
  }

  it('adds two numbers', () => {
    selectFromStreamlitSelectbox('Operation', 'add');
    setNum('A', 5);
    setNum('B', 10);
    cy.contains('button', 'Compute').click();
    cy.contains('Result: 15').should('exist');
  });

  it('divides two numbers', () => {
    selectFromStreamlitSelectbox('Operation', 'div');
    setNum('A', 9);
    setNum('B', 3);
    cy.contains('button', 'Compute').click();
    cy.contains('Result: 3').should('exist');
  });

  it('handles div by zero', () => {
    selectFromStreamlitSelectbox('Operation', 'div');
    setNum('A', 1);
    setNum('B', 0);
    cy.contains('button', 'Compute').click();
    cy.contains('Result: ERROR').should('exist');
  });

  it('clamps correctly', () => {
    selectFromStreamlitSelectbox('Operation', 'clamp');
    setNum('A', 11);
    setNum('B', 0);  // LOW
    cy.get('input[data-testid="stNumberInputField"][aria-label="HIGH (only for clamp; LOW is B)"]').type('{selectall}{backspace}10');
    cy.contains('button', 'Compute').click();
    cy.contains('Result: 10').should('exist');
  });
});
