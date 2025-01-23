# TARGET = client
# SOURCE = client

TARGET = server
SOURCE = server

DIR = ./src/server
OUTPUT_DIR = $(DIR)

UI_DIR = ./src/client
UI_FILES = main_ui

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

ifeq ($(DEBUG),1)
COMPILATION_OUTPUT = 2>$(OUTPUT_DIR)/./"compilation_output_$(@F:.o=).txt"
else
COMPILATION_OUTPUT =
CFLAGS += -fdiagnostics-color=always
endif

all: 	build

build: 	$(OUTPUT_DIR)/./%.o

$(OUTPUT_DIR)/./%.o: 	$(DIR)/./%.c
	$(CC) $(CFLAGS) $< -o $@ $(COMPILATION_OUTPUT)

clean:
	-$(DEL) "$(OUTPUT_DIR)/$(TARGET).o"
	-$(DEL) "$(OUTPUT_DIR)/compilation_output_$(TARGET).txt"

run:	$(OUTPUT_DIR)/./$(TARGET).o
	./$(OUTPUT_DIR)/./$(TARGET).o

gen_ui:	$(UI_DIR)/./$(UI_FILES).py

$(UI_DIR)/./%.py: 	$(UI_DIR)/./%.ui
	$(PY) -m PyQt5.uic.pyuic -x $< -o $@

.DEFAULTGOAL: all
.PHONY: all build clean run gen_ui