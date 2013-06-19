# Requirements

- wget
- beautifulsoup4
    sudo pip install beautifulsoup4

# Update documentation

wget -m http://knockoutjs.com/
cp -R knockoutjs.com/documentation/ KnockoutJS.docset/Contents/Resources/Documents/

# Generate index for documentation

python kodoc2set.py
