/** @type {import('tailwindcss').Config} */
module.exports = {
  // The "content" section tells Tailwind where to look for class names.
  // Tailwind will scan these files and include ONLY the utilities you actually use.
  content: [
    "./website/templates/**/*.html", // ✅ scans your app's templates folder
    "./templates/**/*.html",         // optional: in case you add project-level templates later
    "./static/**/*.js",              // optional: if you use JS with Tailwind classes
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

