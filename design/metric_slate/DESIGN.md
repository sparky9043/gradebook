# Design System Specification: The Academic Atelier

## 1. Overview & Creative North Star
**Creative North Star: The Academic Atelier**
This design system moves away from the sterile, spreadsheet-like nature of traditional gradebooks and toward a "High-End Editorial" experience. It treats student data with the same reverence as a luxury fashion magazine or a premium architectural portfolio. 

The aesthetic is defined by **Soft Minimalism**. We break the "template" look by utilizing intentional asymmetry, breathing room (generous whitespace), and tonal depth. Rather than using rigid lines to contain information, we use sophisticated layering to guide the eye. The result is a workspace that feels like high-quality stationery—tactile, professional, and calm.

---

## 2. Colors: Tonal Architecture
The palette is built on high-quality neutrals that provide comfort during long grading sessions. We strictly avoid pure white (#FFFFFF) for backgrounds to reduce eye strain.

### The "No-Line" Rule
**Explicit Instruction:** 1px solid borders are prohibited for sectioning or containment. 
Boundaries must be defined solely through background color shifts. For example, a `surface_container_low` (#f0f4f7) sidebar sitting on a `surface` (#f7f9fb) background creates a clean, architectural break without the visual "noise" of a line.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. Use the `surface_container` tiers to create "nested" depth:
- **Base Level:** `surface` (#f7f9fb)
- **Secondary Level:** `surface_container_low` (#f0f4f7)
- **Interactive/Floating Level:** `surface_container_lowest` (#ffffff) — Reserved for cards that need to "pop."

### The "Glass & Gradient" Rule
To elevate the experience beyond a standard SaaS tool:
- **Glassmorphism:** Use semi-transparent variants of `surface_container` with a `backdrop-blur` of 20px for floating navigation bars or modal overlays.
- **Signature Textures:** Main CTAs or data-heavy hero headers should utilize a subtle linear gradient (Top-Left to Bottom-Right) transitioning from `primary` (#545f73) to `primary_dim` (#485367). This adds "soul" and a metallic, premium feel.

---

## 3. Typography: The Editorial Voice
Our typography pairing balances authority with approachability.

- **Display & Headlines (Plus Jakarta Sans):** These are our "Voice." With their bold, rounded, yet modern geometry, they echo the "Cubano" aesthetic but with more sophistication. They should be tracked slightly tighter (-0.02em) to feel like a custom-set headline.
- **Body & Labels (Manrope):** This is our "Clarity." Manrope offers exceptional legibility in dense data environments. Use `body-md` for standard student entries and `label-sm` for metadata (like date-stamps or category tags).

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are often too heavy. This system relies on **Tonal Layering** to convey hierarchy.

- **The Layering Principle:** Place a `surface_container_lowest` (#ffffff) card on top of a `surface_container_low` (#f0f4f7) section. This creates a soft, natural lift that mimics paper stacking.
- **Ambient Shadows:** For floating elements (like dropdowns), use a shadow color tinted with the `on_surface` color (#2a3439) at 4-6% opacity. Set the blur to a minimum of 24px to ensure the light feels ambient, not direct.
- **The "Ghost Border" Fallback:** If a border is required for accessibility in data tables, use the `outline_variant` (#a9b4b9) at **10% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons
- **Primary:** Gradient-filled (`primary` to `primary_dim`), `xl` roundedness (1.5rem). Text is `on_primary`.
- **Secondary:** `surface_container_high` background with `on_surface` text. No border.
- **Tertiary:** No background. Use `primary` text weight `title-sm`.

### Cards & Lists
- **Rule:** Forbid the use of divider lines. 
- **Execution:** Separate student rows using vertical whitespace (16px) or by alternating background tones between `surface` and `surface_container_low`. 
- **Grade Cards:** Use `surface_container_highest` (#d9e4ea) for the container and `primary` for the grade text to create a high-contrast focal point.

### Input Fields
- **Default State:** Background `surface_container_low`. No border.
- **Focus State:** Background `surface_container_lowest` with a 1px "Ghost Border" of `primary` at 40% opacity.
- **Error State:** Background `error_container` with `on_error_container` text.

### Chips (Category Tags)
- Use `tertiary_container` for tags like "Late" or "Extra Credit." The roundedness should always be `full` (9999px) to contrast against the more structured cards.

### Progress Gauges (Grade Visualization)
- Instead of thin lines, use thick, soft-capped bars using `primary_fixed_dim` as the track and `primary` as the indicator.

---

## 6. Do’s and Don’ts

### Do:
- **Do** use `surface_bright` to highlight the currently selected student or assignment.
- **Do** use `on_surface_variant` (#566166) for secondary information like "Last Edited" to maintain a hierarchy of importance.
- **Do** maximize whitespace. If a layout feels "busy," increase the padding rather than adding a divider.

### Don't:
- **Don't** use pure black (#000000). Use `on_background` (#2a3439) for all "black" text to keep the editorial feel.
- **Don't** use neon or high-vibrancy colors for status indicators. Use `error` (#9f403d) for failing grades and `tertiary` (#575f75) for passing—it’s more professional.
- **Don't** use sharp corners. Every component must adhere to the **Roundedness Scale**, specifically the `DEFAULT` (0.5rem) or `lg` (1rem) to maintain the "Soft Minimalist" aesthetic.