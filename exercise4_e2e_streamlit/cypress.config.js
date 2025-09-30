const { defineConfig } = require("cypress");
module.exports = defineConfig({
  e2e: {
    baseUrl: "http://localhost:8501",
    supportFile: false,
    video: false,
    defaultCommandTimeout: 15000
  }
});
