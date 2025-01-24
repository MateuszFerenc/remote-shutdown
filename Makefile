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
	openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365

.DEFAULTGOAL: all
.PHONY: all build clean run gen_ui gen_cert run_ssl