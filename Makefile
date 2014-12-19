CFLAGS+=	-W -Wall -I.. -pthread -g

all:
	$(CC) websocket.c tinyweb.c mongoose.c $(CFLAGS) -DUSE_WEBSOCKET -ldl -lutil -o tinyweb;
	$(CC) cgi-getfield.c $(CFLAGS) -o cgi-getfield;
	$(CC) cgi-getcookie.c $(CFLAGS) -o cgi-getcookie;

clean:
	rm -rf tinyweb cgi-getcookie cgi-getfield
