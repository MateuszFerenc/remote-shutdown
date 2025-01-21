TARGET = server
SOURCE = server

DIR = ./src/server
OUTPUT_DIR = $(DIR)

CC = gcc
DEL = rm

CFLAGS += -O2
CFLAGS += -Wfatal-errors
CFLAGS += -Wextra
CFLAGS += -Wall
CFLAGS += -fdiagnostics-color=always
CFLAGS += -pipe
CFLAGS += -Werror=format-security
CFLAGS += -Wundef
CFLAGS += -Wshadow
CFLAGS += -Wpointer-arith
CFLAGS += -Wstrict-prototypes
CFLAGS += -Wswitch-default
CFLAGS += -Wswitch-enum
CFLAGS += -Wunreachable-code

COMPILATION_OUTPUT = 2>$(OUTPUT_DIR)/./"compilation_output_$(@F:.o=).txt"


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