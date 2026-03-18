# AI Lawyer — Indian Constitution Legal Assistant

This repository contains a Flask-based backend and a static frontend for an AI-powered constitutional assistant.

## What this repo contains
- `app.py` — Flask application exposing `/api/consult`, `/api/articles`, and static `index.html` via templates.
- `templates/index.html` — Frontend UI (also can be opened directly via a live server)
- `static/` — JavaScript, CSS and assets
- `constitution_data.json` — Constitution data used by the app
- `requirements.txt` — Python dependencies

## Quick start — development

Prerequisites: Python 3.10+ and `pip`.

Install dependencies:

```pwsh
python -m pip install -r requirements.txt
```

Run Flask server (default):

```pwsh
# start the backend
python app.py
```

Open `http://localhost:5000` in your browser.

Run without starting Flask (serve frontend only via a live/static server):

If you prefer to open just the static frontend (for example using VS Code Live Server) and avoid starting the Flask backend, set the environment variable `SKIP_FLASK=1`.

On Windows PowerShell:

```pwsh
$env:SKIP_FLASK = '1'
$env:OPEN_BROWSER = '1'    # optional — opens templates/index.html in default browser
python app.py
```

When `SKIP_FLASK` is set the script will not start the Flask server. Use your live server (e.g. VS Code Live Server) to serve `templates/index.html` and ensure the frontend uses a relative API path (the repo is configured to do so when not on localhost).

## Publish to GitHub

1. Initialize a repo (if not already):

```pwsh
git init
git add .
git commit -m "Initial commit"
git branch -M main
# create repository on GitHub and add remote
git remote add origin <your-repo-url>
git push -u origin main
```

2. Add a sensible `.gitignore` (already included).

## Deployment options for server/API

- Static frontend only: use GitHub Pages or Netlify to host `templates/index.html` (no backend calls will work unless API is hosted somewhere).
- Full app (frontend + Flask API): deploy the Flask app to a platform such as Render, Railway, Fly, or Heroku. For Heroku, a simple `Procfile` with `web: gunicorn app:app` works (add `gunicorn` to `requirements.txt`).

Example Procfile (Heroku):

```
web: gunicorn app:app
```

## Notes
- Keep any secrets (API keys) out of the repo and use environment variables.
- `requirements.txt` already lists Flask-related packages.

If you want, I can also add a `Procfile`, sample `runtime.txt`, or CI workflow for GitHub Actions to automate deployments.# 🏛️ AI Lawyer - Indian Constitution Legal Assistant

An AI-powered legal consultation application providing intelligent guidance based on the Indian Constitution's 447 articles.

![AI Lawyer](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![License](https://img.shields.io/badge/License-Educational-yellow)

## 🌟 Features

- **AI-Powered Consultation**: Ask legal questions in natural language and receive intelligent, contextual answers
- **Comprehensive Database**: Access all 447 articles of the Indian Constitution
- **Smart Search**: Find articles by number, title, or keywords
- **Interactive Chat Interface**: User-friendly conversation with the AI lawyer
- **Article Browser**: Explore constitutional provisions organized by parts
- **Premium UI Design**: Modern, professional interface with glassmorphism effects
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## 📸 Screenshots

### AI Consultation Interface
Professional chat interface with AI-powered legal advice and constitutional article references.

### Articles Browser
Browse all parts of the Indian Constitution with detailed article information.

## 🚀 Quick Start

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

2. **Navigate to the project directory**:
   ```bash
   cd "ai lawyer"
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 💡 Usage Examples

### Ask Legal Questions
- "What are my fundamental rights?"
- "What is Article 21?"
- "Can I be arrested without a warrant?"
- "What are directive principles?"
- "What is the right to equality?"

### Browse Articles
- Click on "Articles" tab
- Search for specific articles
- Browse by constitutional parts
- View detailed article information

## 📁 Project Structure

```
ai lawyer/
├── app.py                      # Flask backend server
├── constitution_data.json      # Indian Constitution database (447 articles)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/
│   └── index.html             # Main HTML template
└── static/
    ├── style.css              # Premium CSS styling
    └── script.js              # Frontend JavaScript
```

## 🛠️ Technology Stack

### Backend
- **Python 3.x**: Core programming language
- **Flask 3.0.0**: Web framework
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with modern effects
- **JavaScript (ES6+)**: Interactive functionality

### Data
- **JSON**: Constitution database format

## 🎨 Design Features

- **Professional Legal Theme**: Deep blue and gold color scheme
- **Glassmorphism Effects**: Modern card designs with backdrop blur
- **Smooth Animations**: Hover effects and transitions
- **Custom Typography**: Playfair Display for headings, Inter for body text
- **Responsive Layout**: Mobile-first design approach

## 📚 Constitutional Coverage

### Parts Included
- **Part I**: The Union and its Territory
- **Part II**: Citizenship
- **Part III**: Fundamental Rights (Articles 12-35)
- **Part IV**: Directive Principles of State Policy (Articles 36-51)
- **Part IVA**: Fundamental Duties (Article 51A)
- **Part V**: The Union (Articles 52+)
- And all other parts up to Part XXII

### Total Coverage
- **447 Articles**: Complete constitutional text
- **22 Parts**: All major divisions
- **12 Schedules**: Referenced in articles

## 🔒 Legal Disclaimer

⚠️ **Important**: This application is for educational and informational purposes only. It does not constitute legal advice. For specific legal matters, always consult a qualified lawyer or legal professional.

## 🎯 Use Cases

- **Students**: Learn about the Indian Constitution
- **Researchers**: Quick reference for constitutional provisions
- **Citizens**: Understand your fundamental rights
- **Educators**: Teaching tool for constitutional law
- **Legal Enthusiasts**: Explore Indian constitutional framework

## 🔧 API Endpoints

### Consultation
- `POST /api/consult`: Submit legal query and receive AI-generated advice
  - Body: `{"query": "your question"}`
  - Returns: Relevant articles and legal advice

### Articles
- `GET /api/articles`: Get all constitutional parts
- `GET /api/articles?part=III`: Get articles from specific part
- `GET /api/articles?search=keyword`: Search articles
- `GET /api/article/<number>`: Get specific article details

## 🌐 Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 📝 Development

### Adding More Articles
Edit `constitution_data.json` to add or modify articles:
```json
{
  "number": "123",
  "title": "Article Title",
  "text": "Full article text...",
  "keywords": ["keyword1", "keyword2"]
}
```

### Customizing the UI
- Modify `static/style.css` for styling changes
- Edit `templates/index.html` for structure changes
- Update `static/script.js` for functionality changes

## 🤝 Contributing

This is an educational project. Feel free to:
- Report bugs
- Suggest features
- Improve documentation
- Enhance the AI consultation logic

## 📄 License

This project is for educational purposes only. The Indian Constitution text is in the public domain.

## 🙏 Acknowledgments

- Indian Constitution text sourced from official government publications
- Built with Flask, HTML, CSS, and JavaScript
- Designed with modern web development best practices

## 📞 Support

For questions or issues:
1. Check the documentation above
2. Review the code comments
3. Test with different queries
4. Ensure all dependencies are installed

## 🎓 Educational Value

This application demonstrates:
- AI-powered legal technology
- Full-stack web development
- RESTful API design
- Modern UI/UX principles
- Constitutional law accessibility

---

**Made with ⚖️ for legal education and constitutional awareness**

**Version**: 1.0.0  
**Status**: Fully Operational  
**Last Updated**: November 2025
