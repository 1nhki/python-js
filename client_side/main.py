import mymodule
from PySide6.QtWidgets import (QApplication)

app = QApplication([])

main_window = mymodule.window("main")
main_window.setsize([500, 500])

main_layout = mymodule.main_window_layout(main_window)

main_window.show()
app.exec()