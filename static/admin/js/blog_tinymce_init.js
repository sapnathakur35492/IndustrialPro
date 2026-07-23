(function () {
  function initBlogTinyMCE() {
    if (typeof tinymce === 'undefined') {
      return;
    }
    tinymce.remove('textarea.blog-tinymce-editor');
    tinymce.init({
      selector: 'textarea.blog-tinymce-editor',
      height: 520,
      menubar: false,
      branding: false,
      promotion: false,
      plugins: 'lists link table code autoresize',
      toolbar:
        'undo redo | blocks | bold italic underline | ' +
        'alignleft aligncenter alignright | bullist numlist | ' +
        'link table | removeformat | code',
      block_formats: 'Paragraph=p; Heading 2=h2; Heading 3=h3; Heading 4=h4',
      content_style:
        'body { font-family: Inter, system-ui, sans-serif; font-size: 15px; line-height: 1.7; color: #111; }' +
        'h2 { font-size: 1.45rem; color: #102A43; border-bottom: 2px solid rgba(249,115,22,.35); padding-bottom: .35rem; }' +
        'h3 { font-size: 1.2rem; color: #102A43; }' +
        'a { color: #F97316; }',
      convert_urls: false,
      relative_urls: false,
      entity_encoding: 'raw',
      setup: function (editor) {
        editor.on('change keyup', function () {
          editor.save();
        });
      },
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBlogTinyMCE);
  } else {
    initBlogTinyMCE();
  }
})();
