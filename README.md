# 🎮 Endless Runner - Advanced Edition

A feature-rich, responsive endless runner game built with **HTML5 Canvas**, **JavaScript**, and **CSS3**. This advanced edition includes 18+ features including mobile support, power-ups, multiple difficulty levels, character selection, and much more.

## ✨ Features

### Core Gameplay
- **Infinite Gameplay** – Endless procedurally generated obstacles with increasing difficulty
- **Double Jump** – Jump twice in mid-air for better maneuverability
- **3 Difficulty Levels** – Easy, Medium, and Hard with different speeds and obstacle types
- **Multiple Obstacle Types** – Ground obstacles, flying obstacles with animated wings, and tall obstacles

### Power-Ups System
- **🛡 Shield** – Temporary invincibility from obstacles
- **⚡ Speed Boost** – Faster movement for quicker score accumulation
- **⏱ Slow Motion** – Slows down time for easier obstacle dodging
- **❤ Extra Life** – Adds one life (max 5 lives)

### Progression & Scoring
- **Coin Collection** – Collect rotating coins for bonus points
- **Combo System** – Chain coin collections for score multipliers (up to 5x)
- **Health System** – 3 lives with visual heart display
- **Local Leaderboard** – Top 10 scores saved with dates
- **Persistent High Score** – Best score saved across sessions
- **Total Coins Tracker** – Cumulative coin collection

### Visual Effects
- **Parallax Background** – 3-layer scrolling mountains with depth
- **Animated Clouds** – Dynamic cloud movement
- **Day/Night Cycle** – Automatic theme changes every 30 seconds
- **Particle Effects** – Landing, coin collection, and power-up particles
- **Screen Shake** – Impact feedback on damage
- **Flash Effect** – Visual feedback on hits
- **Animated Player** – Squish animation, expressive eyes, and mouth changes

### Customization
- **4 Character Colors** – Blue, Green, Purple, Orange
- **3 Themes** – Day, Night, Sunset color schemes
- **Modern UI** – Glassmorphism effects, gradient buttons, smooth animations

### User Experience
- **Mobile Responsive** – Touch controls and responsive canvas sizing
- **Pause Menu** – Pause/resume functionality (ESC or P key)
- **Clean Menus** – Separate screens for menu, game over, pause, and leaderboard
- **HUD Display** – Real-time score, coins, combo, and active power-ups

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)
- No installation required - runs entirely in the browser

### Running the Game

#### Option 1: Direct File Open
1. Download or clone this repository
2. Open `index.html` in your web browser

#### Option 2: Local Server (Recommended)
```bash
# Using Python
python -m http.server 8000

# Using Node.js (with http-server)
npx http-server

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

#### Option 3: Deploy to Vercel
1. Push this repository to GitHub
2. Import to Vercel
3. Deploy with one click

## 🎯 Controls

### Desktop
- **SPACE** or **Arrow Up** - Jump / Double Jump
- **ESC** or **P** - Pause/Resume game

### Mobile
- **Tap screen** - Jump
- **Jump button** - Jump (bottom of screen)

## 📁 Project Structure

```
Endless_Runner_Game-main/
│
├── index.html              # Main game file (HTML + CSS + JS)
├── README.md               # This file
├── vercel.json             # Vercel deployment configuration
├── package.json            # Project metadata for deployment
│
├── assets/                 # Asset folder (for future images)
│   └── sprites/
│
└── scripts/                # Original Python scripts (legacy)
    ├── background.py
    ├── config.py
    ├── obstacle.py
    ├── particles.py
    └── player.py

```

## 🎮 Game Mechanics

### Difficulty Levels
- **Easy**: Speed 4, spawn rate 2.5s, ground obstacles only
- **Medium**: Speed 6, spawn rate 2s, ground + flying obstacles
- **Hard**: Speed 8, spawn rate 1.5s, ground + flying + tall obstacles

### Scoring
- Base score increases over time
- Coins give +1 coin and increase combo multiplier
- Combo multiplier multiplies score gain
- Higher difficulty = faster score accumulation

### Power-Up Duration
- Shield: 10 seconds
- Speed Boost: 5 seconds
- Slow Motion: 5 seconds

## 🛠️ Customization

### Changing Difficulty
Edit the `DIFFICULTY` object in `CONFIG`:
```javascript
DIFFICULTY: {
    easy: { speed: 4, spawnRate: 2500, obstacleTypes: ['ground'] },
    medium: { speed: 6, spawnRate: 2000, obstacleTypes: ['ground', 'flying'] },
    hard: { speed: 8, spawnRate: 1500, obstacleTypes: ['ground', 'flying', 'tall'] }
}
```

### Adding New Characters
Add to the `CHARACTERS` object:
```javascript
CHARACTERS: {
    blue: '#4169E1',
    green: '#32CD32',
    // Add your color here
    custom: '#FF0000'
}
```

### Modifying Themes
Edit the `THEMES` object:
```javascript
THEMES: {
    day: { sky: '#87CEEB', ground: '#8B4513', groundDark: '#654321' },
    night: { sky: '#1a1a2e', ground: '#2d3436', groundDark: '#636e72' },
    // Add custom theme
}
```

## 📦 Deployment

### Vercel Deployment
1. Push code to GitHub
2. Go to [Vercel](https://vercel.com)
3. Click "New Project"
4. Import your repository
5. Click "Deploy"

The `vercel.json` file is pre-configured for optimal deployment.

### Netlify Deployment
1. Push code to GitHub
2. Go to [Netlify](https://netlify.com)
3. Click "Add new site" → "Import an existing project"
4. Connect to GitHub
5. Deploy

### GitHub Pages
1. Push code to GitHub
2. Go to repository Settings → Pages
3. Select branch (usually `main`)
4. Save

## 🌐 Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🔧 Technical Details

- **Canvas API** for rendering
- **requestAnimationFrame** for smooth 60fps gameplay
- **localStorage** for persistent data
- **CSS3** for modern UI effects
- **Touch Events** for mobile support
- **Responsive Design** with viewport meta tag

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 🎯 Future Enhancements

- [ ] Sound effects and background music
- [ ] More obstacle types and patterns
- [ ] Additional power-ups
- [ ] Achievement system
- [ ] Multiplayer mode
- [ ] More character skins
- [ ] Level progression system

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Built with ❤️ using HTML5, JavaScript, and CSS3**
