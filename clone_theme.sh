#!/usr/bin/env bash
mkdir ~/blue-penguin
rm -rf /tmp/blue-penguin
git clone --depth 1 https://github.com/LukasWoodtli/blue-penguin.git /tmp/blue-penguin
pelican-themes -i /tmp/blue-penguin
