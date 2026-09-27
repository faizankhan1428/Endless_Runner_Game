# 🎮 Endless Runner - Ultimate Edition

A feature-rich, professional-grade endless runner game built with **HTML5 Canvas**, **JavaScript**, and **CSS3**. This ultimate edition includes 30+ advanced features including mobile support, power-ups, multiple difficulties, character selection, daily challenges, achievements, and much more.

![Game Preview](Game/game.gif)

## ✨ Features

### Core Gameplay
- **Infinite Gameplay** – Endless procedurally generated obstacles with increasing difficulty
- **Double Jump** – Jump twice in mid-air for better maneuverability (upgradeable to Triple Jump)
- **3 Difficulty Levels** – Easy, Medium, and Hard with different speeds and obstacle types
- **Multiple Obstacle Types** – Ground obstacles, flying obstacles with animated wings, and tall obstacles
- **Full Screen Layout** – Game fills entire screen on all devices (mobile, tablet, desktop, PC)

### Power-Ups System
- **🛡 Shield** – Temporary invincibility from obstacles (10 seconds)
- **⚡ Speed Boost** – Faster movement for quicker score accumulation (5 seconds)
- **⏱ Slow Motion** – Slows down time for easier obstacle dodging (5 seconds)
- **❤ Extra Life** – Adds one life (max 5 lives)
- **Spawn Indicators** – Visual warnings before power-ups spawn

### Progression & Scoring
- **Coin Collection** – Collect rotating coins for bonus points
- **Combo System** – Chain coin collections for score multipliers (up to 5x) with visual indicators
- **Health System** – 3 lives with visual heart display (upgradeable)
- **Local Leaderboard** – Top 10 scores saved with dates
- **Persistent High Score** – Best score saved across sessions
- **Total Coins Tracker** – Cumulative coin collection
- **Score Milestones** – Automatic coin rewards at score milestones (100, 250, 500, 750, 1000, etc.)
- **Daily Challenges** – New challenge every day with coin rewards
- **Streak System** – Track consecutive days of playing with rewards

### Visual Effects
- **Simplified Background** – Clean sky gradient with seamless scrolling for optimal full-screen performance
- **Animated Clouds** – Dynamic cloud movement across the sky
- **Animated Birds** – Flying birds with wing flapping animation
- **Day/Night Cycle** – Automatic theme changes every 30 seconds
- **Particle Effects** – Landing, coin collection, and power-up particles
- **Screen Shake** – Impact feedback on damage
- **Flash Effect** – Visual feedback on hits
- **Animated Player** – Professional character with head, body, arms, legs, feet, expressive eyes, and mouth
- **Weather Effects** – Rain and snow particle systems
- **Combo Visuals** – On-screen combo multiplier display
- **Obstacle Warnings** – Visual alerts before obstacles spawn

### Customization
- **4 Character Colors** – Blue, Green, Purple, Orange
- **3 Themes** – Day, Night, Sunset color schemes
- **Modern UI** – Glassmorphism effects, gradient buttons, smooth animations
- **Settings Menu** – Toggle sound, weather, particles, and dark mode

### Shop System
- **Coin Shop** – Spend collected coins on upgrades
- **6 Shop Items**:
  - Extra Life (50 coins) – Start with 4 lives
  - Coin Magnet (100 coins) – Attract coins from nearby
  - Triple Jump (150 coins) – Jump up to 3 times
  - Shield Start (200 coins) – Start with shield active
  - Rainbow Mode (300 coins) – Rainbow color trail effect
  - Neon Glow (250 coins) – Neon glow effect on player

### Achievements System
- **10 Achievements** – Unlock badges for various accomplishments:
  - 👶 First Steps – Complete your first run
  - 💯 Century – Score 100 points
  - 🏆 High Scorer – Score 500 points
  - 👑 Master – Score 1000 points
  - 💰 Coin Collector – Collect 100 total coins
  - 💎 Rich – Collect 500 total coins
  - 🔥 Week Warrior – 7 day playing streak
  - ⭐ Monthly Legend – 30 day playing streak
  - 💪 Hardcore – Complete a run on Hard difficulty
  - ⚡ Perfect – Complete a run without losing a life
- **Achievement Notifications** – Pop-up alerts when achievements are unlocked

### Statistics Dashboard
- **Games Played** – Total number of games played
- **High Score** – Personal best score
- **Total Coins** – Lifetime coin collection
- **Total Distance** – Total distance run
- **Current Streak** – Consecutive days played
- **Achievements Progress** – Track unlocked achievements

### User Experience
- **Mobile Responsive** – Touch controls and responsive canvas sizing
- **Pause Menu** – Pause/resume functionality (ESC or P key)
- **Clean Menus** – Separate screens for menu, game over, pause, leaderboard, shop, stats, settings
- **HUD Display** – Real-time score, coins, combo, active power-ups, and warnings
- **Touch Controls** – "JUMP" button for mobile devices (replaced arrow)
- **Settings** – Customize game experience with toggles

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
2. Go to [Vercel](https://vercel.com)
3. Click "New Project"
4. Import your repository
5. Click "Deploy"

## 🎯 Controls

### Desktop
- **SPACE** or **Arrow Up** - Jump / Double Jump
- **ESC** or **P** - Pause/Resume game

### Mobile
- **Tap screen** - Jump

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
│   └─ sprites/
│
└── scripts/                # Original Python scripts (legacy)
    ├── background.py
    ├── config.py
    ├── obstacle.py
    ├── particles.py
    └─ player.py
```

## 🎮 Game Mechanics

### Difficulty Levels
- **Easy**: Speed 4, spawn rate 2.5s, ground obstacles only
- **Medium**: Speed 6, spawn rate 2s, ground + flying obstacles
- **Hard**: Speed 8, spawn rate 1.5s, ground + flying + tall obstacles

### Scoring
- Base score increases over time
- Coins give +1 coin and increase combo multiplier
- Combo multiplier multiplies score gain (up to 5x)
- Higher difficulty = faster score accumulation
- Score milestones award bonus coins

### Power-Up Duration
- Shield: 10 seconds
- Speed Boost: 5 seconds
- Slow Motion: 5 seconds

### Daily Challenges
- New challenge generates every day
- Complete challenges for bonus coins
- Challenge types: Coin collection, Score targets, Distance goals

### Streak System
- Play consecutive days to build streak
- Streaks unlock achievements
- Streaks are tracked in statistics

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

### Adding Shop Items
Add to the `SHOP_ITEMS` object:
```javascript
SHOP_ITEMS: {
    customItem: { name: 'Custom Item', price: 500, icon: '🎁', description: 'Custom effect' }
}
```

### Adding Achievements
Add to the `ACHIEVEMENTS` object:
```javascript
ACHIEVEMENTS: {
    customAchievement: { 
        name: 'Custom Achievement', 
        icon: '🏅', 
        description: 'Custom description',
        condition: (stats) => stats.highScore >= 10000 
    }
}
```

## 📦 Deployment

### Vercel Deployment
1. Push code to GitHub
2. Go to [Vercel](https://vercel.com)
3. Click "New Project"
4. Import your repository
5. Click "Deploy"

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
- **localStorage** for persistent data (scores, coins, achievements, settings)
- **CSS3** for modern UI effects
- **Touch Events** for mobile support
- **Responsive Design** with viewport meta tag
- **CSS Animations** for notifications and effects

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 🎯 Features Summary

**30+ Advanced Features:**
1. ✅ Full screen responsive layout
2. ✅ Professional animated character
3. ✅ Coin shop with 6 purchasable items
4. ✅ Daily challenges system
5. ✅ Playing streak tracking
6. ✅ Statistics dashboard
7. ✅ Settings menu
8. ✅ Weather effects (rain, snow)
9. ✅ Achievement badges (10 achievements)
10. ✅ Combo visual effects
11. ✅ Power-up spawn indicators
12. ✅ Obstacle preview warnings
13. ✅ Score milestone rewards
14. ✅ Sound toggle
15. ✅ Double jump (upgradeable to triple)
16. ✅ 3 difficulty levels
17. ✅ Multiple obstacle types
18. ✅ Power-ups (4 types)
19. ✅ Coin collection
20. ✅ Health system
21. ✅ Local leaderboard
22. ✅ High score persistence
23. ✅ Total coins tracking
24. ✅ Parallax background
25. ✅ Day/night cycle
26. ✅ Particle effects
27. ✅ Screen shake
28. ✅ Flash effects
29. ✅ 4 character colors
30. ✅ 3 themes
31. ✅ Pause menu
32. ✅ Mobile touch controls
33. ✅ HUD display

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Built with ❤️ using HTML5, JavaScript, and CSS3**
