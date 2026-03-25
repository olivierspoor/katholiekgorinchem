---
hide:
  - footer
  - navigation
---
<script>
document.addEventListener("DOMContentLoaded", init);
document.addEventListener("md-content-loaded", init);

function init() {
  console.log("INIT");

  const posts = document.querySelectorAll(".md-post");

  posts.forEach((post, index) => {
    console.log(`--- Post ${index} ---`);

    const img = post.querySelector(".md-author img");
    if (!img) {
      console.log("❌ No author image");
      return;
    }

    const alt = img.getAttribute("alt");
    if (!alt) {
      console.log("❌ No alt");
      return;
    }

    console.log("Author:", alt);

    const metaList = post.querySelector(".md-meta__list");
    if (!metaList) {
      console.log("❌ No meta list");
      return;
    }

    // Prevent duplicates
    if (metaList.querySelector(".author-injected")) {
      console.log("⚠️ Already added");
      return;
    }

    const li = document.createElement("li");
    li.className = "md-meta__item author-injected";
    li.textContent = alt;

    metaList.prepend(li);
    console.log("✅ Added to meta list");
  });
}

</script>
<style>

  .img-caption {
  font-size: 0.9em;
  color: #666;
  text-align: center;
  margin-top: 0.3em;
  margin-bottom: 1em;
}
</style>
# Berichten