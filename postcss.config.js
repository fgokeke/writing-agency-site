// PostCSS config file.
// Think of this as a "pipeline" for processing your CSS
// Each plugin listed here modifies your CSS in some way.

const autoprefixer = require("autoprefixer");

module.exports = {
    plugins: {
        // Tailwind plugin: expands @tailwind directives into real CSS classes.
        tailwindcss: {},
        // Autoprefixer plugin: adds vendor prefixes for older browsers (e.g., -webkit-)
        autoprefixer: {},
    }
}
