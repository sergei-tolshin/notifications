X_FRAME_OPTIONS = 'SAMEORIGIN'
TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'width': 960,
    'relative_urls': False,
    'convert_urls': True,
    'file_picker_callback': 'FileBrowserPopup',
    'plugins': '''
        print preview paste importcss searchreplace autolink autosave save directionality code visualblocks
        visualchars fullscreen image link media table charmap hr pagebreak nonbreaking anchor toc
        insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars
        ''',
    # 'menubar': 'file edit view insert tools',
    'menubar': False,
    'toolbar': '''
        undo redo | bold italic underline removeformat | fontsizeselect formatselect | alignleft aligncenter alignright 
        | outdent indent | numlist bullist table | insertfile image media link | blockquote hr nonbreaking charmap | 
        wordcount print fullscreen preview code
        ''',
    'toolbar_mode': 'sliding',
    'toolbar_sticky': True,
    'file_picker_types': 'image',
    'image_advtab': True,
    'importcss_append': True,
    'branding': False,
    'block_formats': 'Параграф=p; Блок=div; Заголовок 3=h3; Заголовок 4=h4; Заголовок 5=h5; Заголовок 6=h6',
    'fontsize_formats': '10px 12px 14px 15px 16px 18px 20px 24px 36px',
    'content_style': 'body { font-family:Montserrat,Museo,-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif; font-size:15px }'
}