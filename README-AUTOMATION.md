# Gugnani & Co website source
- `build.py` (+ `global_data.py`, `global_gen.py`) generates the whole static site into `./gugnaniandco/`.
- Weekly blog posts live in `blog_posts.json` (newest FIRST). Each entry: slug, date (YYYY-MM-DD), title, desc, paras (list of HTML paragraph strings; a string starting with `<ul` is output as-is, use `<ul class="ticks">`).
- To publish: add the entry at the top of `blog_posts.json`, then run `./publish.sh "Add blog: <title>"`. It rebuilds, pushes source to branch `source` and the built site to branch `main` (Cloudflare Pages auto-deploys `main` to gugnaniandco.com).
- Rules: never claim the firm is "best"/"No.1" (ICAI rules); no invented client names or figures; facts on law changes must come from sources checked that day.

## Facebook post images
`node fbposts/post_image.js spec.json out.png` renders a 1080x1080 branded image with the CA India logo (needs the pre-installed playwright). See the header of that file for the spec format.
