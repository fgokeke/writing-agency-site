/** @type {import('tailwindcss').Config} */
module.exports = {
  // The "content" section tells Tailwind where to look for class names.
  // Tailwind will scan these files and include ONLY the utilities you actually use.
  content: [
    "./templates/**/*.html",    // scans project-level templates (e.g. /templates/base.html)
    "./**/templates/**/*.html"  // scans app-level templates inside each Django app
  ],
  theme: {
    // "extend" is where you add custom values (colors, fonts, spacing, etc.)
    extend: {
      // Example: uncomment to add a custom color
      // colors: {
      //  brand: "#1da1f2"
      // }
    },
  },
  // Tailwind plugins can go here (forms, typography, etc.)
  plugins: [],
}

