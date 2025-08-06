# 🌍 TerraLedger — Frontend for TerraLedger Carbon Exchange
**TerraLedger** is the eco-inspired, community-first frontend of **TerraLedger Carbon Exchange**, Africa’s first AI-powered, blockchain-based carbon credit marketplace. We enable transparent, real-time, and verifiable carbon offsetting - built on Hedera and designed to empower individuals, businesses, and communities to take climate action.
---

## 🔥 Why TerraLedger?

Traditional carbon markets are plagued with greenwashing, opacity, and exclusion of local/domestic emissions. TerraLedger reimagines this by:

- 🛰️ Leveraging **AI & satellite data** for live verification
- ♻️ Tokenizing carbon sequestration into **dynamic Carbon NFTs**
- 🌍 Including **household/domestic emissions** into offsetting strategies
- ⚖️ Enabling **fractional retirement** and **ZK-audited transparency**
- 🇳🇬 Centering **Africa and underserved regions** in climate finance

---

## ✨ Features

### 🏠 Landing Page
- Immersive African landscape hero
- Clear mission and CTAs: *Offset Carbon*, *Join as Project*, *Learn More*

### 🌿 Carbon Marketplace
- Browse Carbon NFTs (credits) verified by AI & satellite
- View live progress and ratings
- Micro-credit purchasing system

### 📊 User Dashboard
- Track personal carbon impact
- View purchased credits and retirement certificates
- Earn achievements for reduction milestones

### 🔍 Emission Tracker
- Calculate domestic emissions (e.g., generator, cooking fuel)
- Get actionable suggestions to reduce your footprint

### 🗺️ Live Map Integration
- Display carbon projects with real-time status (active, retired, at risk)
- Integrated with Hedera Mirror Node API

### 📚 Learning Hub
- Explore resources on carbon markets, sustainability, and African climate issues

---

## 🛠 Tech Stack

| Layer             | Technology                           |
|------------------|---------------------------------------|
| Frontend          | React + Vite + TypeScript             |
| UI Framework      | Tailwind CSS + shadcn-ui              |
| Maps              | React Leaflet / Mapbox (for project tracking) |
| Animations        | Framer Motion                         |
| APIs              | Supabase (for auth & data) + Hedera Mirror Node |
| Blockchain Layer  | Hedera Hashgraph (HTS, HCS, Guardian) |
| ZK-Proofs         | Circom (via backend integration)      |

---

## 📦 Getting Started

### Prerequisites

- Node.js ≥ 18
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/terreledger.git
cd terraledger

# Install dependencies
npm install

# Run locally
npm run dev
````

The app should now be running at [http://localhost:5173](http://localhost:5173)

---

## 🧪 Available Scripts

```bash
npm run dev       # Start the development server
npm run build     # Build the app for production
npm run preview   # Preview the production build
```

---

## 🧩 Project Structure

```
src/
├── components/      # Reusable UI components (cards, headers, etc.)
├── pages/           # App pages (Landing, Marketplace, Dashboard, etc.)
├── api/             # API calls to Hedera / Supabase
├── lib/             # Utility functions (formatting, hooks)
├── assets/          # Images, icons, svgs
├── styles/          # Tailwind configuration and global CSS
```

## 🤝 Contribution

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

---

## 🔐 Environment Variables

To run Terraledger, create a `.env` file in the root and include:

```env
VITE_SUPABASE_URL=your-supabase-project-url
VITE_SUPABASE_KEY=your-supabase-anon-key
VITE_HEDERA_API_URL=your-mirror-node-endpoint

```

> TerraLedger is not just a product — it’s a movement to put African communities at the center of global climate solutions. 🌍♻️🚀

