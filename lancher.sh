#!/bin/bash

echo "🔥 Welcome to BlazeOS 26 🔥"
echo "Launching cinematic shell..."

# Start menu logic
echo "[Start Menu]"
echo "1. MicroArcade"
echo "2. Settings"
echo "3. Exit"

read -p "Choose an option: " choice

case $choice in
  1) echo "Launching MicroArcade..."; exec microarcade ;;
  2) echo "Opening Settings..."; exec blaze-settings ;;
  3) echo "Goodbye!" ;;
  *) echo "Invalid choice." ;;
esac
