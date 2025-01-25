TARGET = server

TARGET_SSL = server_ssl

DIR = ./src/server
OUTPUT_DIR = $(DIR)

UI_DIR = ./src/client
UI_FILES = $(wildcard $(UI_DIR)/*.ui)
UI2PY_FILES = $(UI_FILES:.ui=.py)

CC = gcc
DEL = rm
PY = python3
SSL = openssl

CFLAGS += -O3
CFLAGS += -Wfatal-errors
# CFLAGS += -Wextra
CFLAGS += -Wall
CFLAGS += -pipe
CFLAGS += -Wformat
CFLAGS += -Werror=format-security
CFLAGS += -Wundef
CFLAGS += -Wshadow
CFLAGS += -Wpointer-arith
CFLAGS += -Wstrict-prototypes
CFLAGS += -Wswitch-default
CFLAGS += -Wswitch-enum
CFLAGS += -Wunreachable-code
# CFLAGS += -std=c17

LDFLAGS += -lssl -lcrypto

SSL_CAROOT_DESC = "/C=PL/ST=Wlkp/L=Poznan/O=none/CN=RemoteShutdown"
SSL_CASERVER_DESC = "/C=PL/ST=Wlkp/L=Poznan/O=none/CN=server.RemoteShutdown"
SSL_CACLIENT_DESC = "/C=PL/ST=Wlkp/L=Poznan/O=none/CN=client.RemoteShutdown"

ifeq ($(DEBUG),1)
COMPILATION_OUTPUT = 2>$(OUTPUT_DIR)/./"compilation_output_$(@F:.o=).txt"
else
COMPILATION_OUTPUT =
CFLAGS += -fdiagnostics-color=always
endif

all: 	build

build: 	$(OUTPUT_DIR)/./$(TARGET).o

$(OUTPUT_DIR)/./%.o: 	$(DIR)/./%.c
	$(CC) $(CFLAGS) $< $(LDFLAGS) -o $@ $(COMPILATION_OUTPUT)

clean:
	-$(DEL) "$(OUTPUT_DIR)/$(TARGET).o"
	-$(DEL) "$(OUTPUT_DIR)/compilation_output_$(TARGET).txt"

run:	$(OUTPUT_DIR)/./$(TARGET).o
	./$(OUTPUT_DIR)/./$(TARGET).o

run_ssl:	$(OUTPUT_DIR)/./$(TARGET_SSL).o
	./$(OUTPUT_DIR)/./$(TARGET_SSL).o

gen_ui:	$(UI2PY_FILES)

%.py: %.ui
	$(PY) -m PyQt5.uic.pyuic -x $< -o $@

gen_cert:
	$(SSL) req -x509 -nodes -days 365 -newkey rsa:4096 -keyout ca_key.pem -out ca_cert.pem -subj $(SSL_CAROOT_DESC)

	$(SSL) genrsa -out server_key.pem 4096
	$(SSL) req -new -key server_key.pem -out server_cert.csr -subj $(SSL_CASERVER_DESC)
	$(SSL) x509 -req -days 120 -in server_cert.csr -CA ca_cert.pem -CAkey ca_key.pem -CAcreateserial -out server_cert.pem

	$(SSL) genrsa -out client_key.pem 4096
	$(SSL) req -new -key client_key.pem -out client_cert.csr -subj $(SSL_CACLIENT_DESC)
	$(SSL) x509 -req -days 120 -in client_cert.csr -CA ca_cert.pem -CAkey ca_key.pem -CAcreateserial -out client_cert.pem

clean_certs:
	-$(DEL) *.pem
	-$(DEL) *.csr
	-$(DEL) *.srl

.DEFAULTGOAL: all
.PHONY: all build clean run gen_ui gen_cert run_ssl clean_certs