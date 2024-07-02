import fitz

sra_form = 'PLUP Inspection Report.pdf'

document = fitz.open(sra_form)

font_rgb = (0, 137, 218)
font_color = tuple(value / 255 for value in font_rgb)

for page_num in range(len(document)):
    page = document.load_page(page_num)
    for indx, field in enumerate(page.widgets()):
        if field.field_type == fitz.PDF_WIDGET_TYPE_TEXT:
            field.field_value = '{0}_{1}'.format(indx, field.field_type)
            field.update()
        elif field.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
            field.field_value = True
            field.update()
            page.insert_text(field.rect.tl, "This is the index: {0}".format(indx), fontsize=12, color=font_color)

document.save('applications_index.pdf')
