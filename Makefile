# TARGET = client
# SOURCE = client

TARGET = server
SOURCE = server

DIR = ./src/server
OUTPUT_DIR = $(DIR)

CC = gcc
DEL = rm

CFLAGS += -O2
CFLAGS += -Wfatal-errors
# CFLAGS += -Wextra
# CFLAGS += -Wall
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

ifeq ($(DEBUG),1)
COMPILATION_OUTPUT = 2>$(OUTPUT_DIR)/./"compilation_output_$(@F:.o=).txt"
else
COMPILATION_OUTPUT =
CFLAGS += -fdiagnostics-color=always
endif

all: 	build

build: 	$(OUTPUT_DIR)/./$(TARGET).o

$(OUTPUT_DIR)/./$(TARGET).o: 	$(DIR)/./$(SOURCE).c
	$(CC) $(CFLAGS) $< -o $@ $(COMPILATION_OUTPUT)

clean:
	-$(DEL) "$(OUTPUT_DIR)/$(TARGET).o"
	-$(DEL) "$(OUTPUT_DIR)/compilation_output_$(TARGET).txt"

run:	$(OUTPUT_DIR)/./$(TARGET).o
	./$(OUTPUT_DIR)/./$(TARGET).o

.DEFAULTGOAL: all
.PHONY: all build clean run