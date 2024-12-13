import uno

def inputbox(message, title="", default="", x=None, y=None):
    """ Shows dialog with input box. """
    WIDTH = 600
    HORIZONTAL_MARGIN = VERTICAL_MARGIN = 8
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 26
    HORIZONTAL_SEP = VERTICAL_SEP = 8
    LABEL_HEIGHT = BUTTON_HEIGHT * 2 + 5
    EDIT_HEIGHT = 24
    HEIGHT = VERTICAL_MARGIN * 2 + LABEL_HEIGHT + VERTICAL_SEP + EDIT_HEIGHT
    ctx = uno.getComponentContext()
    def create(name):
        return ctx.getServiceManager().createInstanceWithContext(name, ctx)
    dialog = create("com.sun.star.awt.UnoControlDialog")
    dialog_model = create("com.sun.star.awt.UnoControlDialogModel")
    dialog.setModel(dialog_model)
    dialog.setVisible(False)
    dialog.setTitle(title)
    dialog.setPosSize(0, 0, WIDTH, HEIGHT, SIZE)
    def add(name, type, x_, y_, width_, height_, props):
        model = dialog_model.createInstance("com.sun.star.awt.UnoControl" + type + "Model")
        dialog_model.insertByName(name, model)
        control = dialog.getControl(name)
        control.setPosSize(x_, y_, width_, height_, POSSIZE)
        for key, value in props.items():
            setattr(model, key, value)
    label_width = WIDTH - BUTTON_WIDTH - HORIZONTAL_SEP - HORIZONTAL_MARGIN * 2
    add("label", "FixedText", HORIZONTAL_MARGIN, VERTICAL_MARGIN, label_width, LABEL_HEIGHT, 
        {"Label": str(message), "NoLabel": True})
    add("btn_ok", "Button", HORIZONTAL_MARGIN + label_width + HORIZONTAL_SEP, VERTICAL_MARGIN, 
            BUTTON_WIDTH, BUTTON_HEIGHT, {"PushButtonType": OK, "DefaultButton": True})
    add("btn_cancel", "Button", HORIZONTAL_MARGIN + label_width + HORIZONTAL_SEP, VERTICAL_MARGIN + BUTTON_HEIGHT + 5, 
            BUTTON_WIDTH, BUTTON_HEIGHT, {"PushButtonType": CANCEL})
    add("edit", "Edit", HORIZONTAL_MARGIN, LABEL_HEIGHT + VERTICAL_MARGIN + VERTICAL_SEP, 
            WIDTH - HORIZONTAL_MARGIN * 2, EDIT_HEIGHT, {"Text": str(default)})
    frame = create("com.sun.star.frame.Desktop").getCurrentFrame()
    window = frame.getContainerWindow() if frame else None
    dialog.createPeer(create("com.sun.star.awt.Toolkit"), window)
    if not x is None and not y is None:
        ps = dialog.convertSizeToPixel(uno.createUnoStruct("com.sun.star.awt.Size", x, y), TWIP)
        _x, _y = ps.Width, ps.Height
    elif window:
        ps = window.getPosSize()
        _x = ps.Width / 2 - WIDTH / 2
        _y = ps.Height / 2 - HEIGHT / 2
    edit = dialog.getControl("edit")
    edit.setSelection(uno.createUnoStruct("com.sun.star.awt.Selection", 0, len(str(default))))
    edit.setFocus()
    ret = edit.getModel().Text if dialog.execute() else ""
    dialog.dispose()
    return ret

def insert_hello_world():
    llista = inputbox("Insereix la llista de persones les quals rebran el diploma", "Llistat persones", "Joan Gomila, Toni Pons, Pere Gomila")

    llista = llista.split(",")
    
    document = XSCRIPTCONTEXT.getDocument()
    search = document.createSearchDescriptor()
    search.SearchString = "{name}"
    search.SearchAll = True
    search.SearchWords = True
    search.SearchCaseSensitive = False
    selsFound = document.findAll(search)
    
    if selsFound.getCount() == 0:
        return "No se han encontrado las marcas '{name}' en el documento."
    
    if selsFound.getCount() != len(llista):
        return f"Advertencia: Se encontraron {selsFound.getCount()} marcas, pero solo se proporcionaron {len(llista)} nombres."

    for selIndex in range(0, selsFound.getCount()):
        selFound = selsFound.getByIndex(selIndex)
        selFound.setString(llista[selIndex].strip())

    return "Los diplomas han sido generados correctamente."

insert_hello_world()
