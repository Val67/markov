#!/bin/sh
cat logs/* | grep "<aaaa>" | cut -c 28- > corpus
