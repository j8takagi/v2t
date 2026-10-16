PREFIX ?= ~
BINDIR := $(PREFIX)/bin

.PHONY: all clean install uninstall

all:
	# コンパイルが必要な場合はここに記述（スクリプトなら何もしない）

install:
	install -d $(DESTDIR)$(BINDIR)
	install -m 755 v2t.py $(DESTDIR)$(BINDIR)/v2t

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/v2t
