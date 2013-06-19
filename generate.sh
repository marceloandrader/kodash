#!/bin/bash

wget -m http://knockoutjs.com/
rm -r KnockoutJS.docset/Contents/Resources/Documents/*
CSS=$(cat <<EOT
div.leftCol { position: absolute; width: 16em; padding-top: 1em; display: none; } 
div.rightCol { margin-left: 1em; width: 52em; }
.main-menu { display: none; }
.vspace { height: 0 !important;}
#wrapper { width: 890px !important;}
EOT)
echo $CSS >> knockoutjs.com/css/styles.css
tail knockoutjs.com/css/styles.css
cp -R knockoutjs.com/ KnockoutJS.docset/Contents/Resources/Documents/
python kodoc2set.py
