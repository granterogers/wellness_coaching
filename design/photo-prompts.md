# Photo mock-ups: prompts for an AI image tool

Purpose: make rough mock-ups of the eight photos the site needs, from Grant's own photos, to hand to a photographer
as a visual brief. They are **not** for the live site: AI images drift from your real face and body, get hands and
poses wrong, and would show things that never happened. The full brief for each slot is in
`knowledge/photo-slots.md`; the photographer should get both.

## How to do it

1. Pick an image tool that accepts your own photos as a reference (for example ChatGPT's image generation or Google
   Gemini; Midjourney works too with a character reference). Use your own account.
2. Upload 3–5 clear photos of yourself: face straight on, face in profile, and one or two full-length. Plain
   clothes, good light. **Don't put these in this repository** (it's public).
3. Paste the shared style line, then one slot's prompt. Generate a few, keep the closest, and note what's wrong
   ("too posed", "light too cold") for the photographer.
4. Ask for the stated shape (square, 4:5, 3:2, 16:9) so the mock-up matches the slot.

**Shared style (paste first every time):**
> Use the person in my reference photos; keep their face, build and age exactly. Documentary photograph, natural
> light, real place, slightly warm colour grade, calm and unposed. Plain tonal clothing in ink, stone or olive, no
> logos. No text, no filters, no studio backdrop.

## The eight photos

| Slot | Shape | Prompt |
|---|---|---|
| P03 Portrait (home About + About page) | 4:5 vertical | Chest-up portrait looking straight into the camera, warm and approachable, slight smile. Plain light wall or soft outdoor background, even daylight. |
| P04 Profile (About page) | 4:5 vertical | Head-and-shoulders side profile, thoughtful and serious. Hard side light from a window, dark background. Black and white. |
| P06 Online coaching (Programme) | 3:2 horizontal | Over-the-shoulder view of the person on a video call at a home desk, laptop screen visible with the other person blurred. Natural window light. |
| P07 Calm pillar | 1:1 square | Close-up of the torso, one hand resting on the ribs, eyes closed if the face shows. Soft indoor light, slow and quiet. |
| P08 Strength pillar | 1:1 square | Full body in a mobility posture such as a deep squat or hip opener on a wooden floor or terrace. Morning light; strong, fluid, unforced. |
| P10 Sleep pillar | 1:1 square | Seen from directly above, lying on the back under a blanket in Yoga Nidra, eyes closed. Dim, warm evening light; deep rest. |
| P11 Energy pillar | 1:1 square | Medium-wide outdoors, mid-movement (carrying, climbing or swimming) on a coast or mountain. Bright natural light, energetic and capable; nothing sexual or suggestive. |
| P16 Water texture (night section background) | 16:9 horizontal | No people. Calm water surface at dusk, low contrast and little detail, so text can sit on top when it's darkened. |

## For the photographer

Send the chosen mock-ups with `knowledge/photo-slots.md`, and say they show the **framing, light and mood**, not the
exact look. Ask for each photo in the shape above, plus an uncropped original; for P03, also a horizontal version.

## All eight in one go (ChatGPT)

Upload 5–10 photos of yourself first (face straight on, side profile, one or two full-length; good light, no
sunglasses), then paste the prompt below. The site crops each image to its slot, so ChatGPT's square, tall and wide
sizes all work. Name each download exactly as given and upload it to `src/assets/photos/` (`CONTENT-EDITING.md` →
Photos). Replace them with real photos before launch (`LAUNCH-CHECKLIST.md`).

```
I'm building my coaching website and need 8 placeholder photos of me. The photos I've uploaded are only a reference
for my face, hair, build, skin tone and age: keep my likeness as close to them as you can.

Every image should look like a real documentary photograph: natural light, real places, a slightly warm colour
grade, calm and unposed. Plain clothes in dark ink, stone or olive tones, no logos. Natural hands and anatomy.
No text, watermarks, borders, filters or studio backdrops.

Make the images one at a time, in this order. After each one, tell me its file name, then wait for me to say "next"
(or ask for changes) before making the next.

1. about-portrait (tall): me from the chest up, looking straight into the camera, warm and approachable, slight
   smile. Plain light wall or soft outdoor background, even daylight.
2. about-profile-bw (tall, black and white): head and shoulders in side profile, thoughtful and serious. Hard side
   light from a window, dark background.
3. work-call (wide): over-the-shoulder view of me on a video call at a home desk; the laptop screen shows another
   person, blurred. Notebook and pen on the desk. Natural window light.
4. pillar-breathe (square): close-up of my torso, one hand resting on my ribs, eyes closed if my face is in frame.
   Soft indoor light; slow and quiet.
5. pillar-move (square): full body in a mobility posture (a deep squat or a hip opener) on a wooden floor or terrace.
   Morning light; strong, fluid, unforced.
6. pillar-restore (square): seen from directly above, me lying on my back under a blanket with my eyes closed, as in
   Yoga Nidra. Dim, warm evening light; deep rest.
7. pillar-vitality (square): me outdoors mid-movement (carrying something heavy, climbing rocks or swimming) on a
   coast or mountain. Bright natural light; energetic and capable. Nothing sexual or suggestive.
8. texture-water (wide): no people. A calm water surface at dusk, low contrast and little detail, so text can sit on
   top of it.
```
