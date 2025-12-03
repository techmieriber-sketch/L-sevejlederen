# Guide til at få GitHub Pages til at virke

## Problem
GitHub Pages udgiver ikke din side. Dette skyldes typisk en af følgende årsager:

## Løsning - Følg disse trin:

### 1. Installer Git (hvis ikke allerede installeret)
- Download Git fra: https://git-scm.com/download/win
- Installer og genstart din terminal/editor

### 2. Opret en GitHub repository
1. Gå til https://github.com og log ind
2. Klik på "+" i øverste højre hjørne → "New repository"
3. Navngiv repository (fx "laesevejlederen")
4. Vælg "Public" (gratis GitHub Pages kræver public repository)
5. **IKKE** vælg "Initialize with README"
6. Klik "Create repository"

### 3. Initialiser Git i dit projekt
Åbn PowerShell eller Terminal i mappen `Læsevejlederen` og kør:

```powershell
# Initialiser git repository
git init

# Tilføj alle filer
git add .

# Lav første commit
git commit -m "Første commit - Læsevejlederen"

# Tilføj din GitHub repository som remote (erstatt med dit repository navn)
git remote add origin https://github.com/DIT-BRUGERNAVN/DIT-REPOSITORY-NAVN.git

# Push til GitHub
git branch -M main
git push -u origin main
```

### 4. Aktiver GitHub Pages
1. Gå til din repository på GitHub
2. Klik på "Settings" (indstillinger)
3. Scroll ned til "Pages" i venstre menu
4. Under "Source" vælg:
   - Branch: `main`
   - Folder: `/ (root)`
5. Klik "Save"
6. Vent 1-2 minutter, og din side vil være tilgængelig på:
   `https://DIT-BRUGERNAVN.github.io/DIT-REPOSITORY-NAVN/`

### 5. Vigtige krav for GitHub Pages
✅ `index.html` skal være i roden af repository (✓ du har det)
✅ Alle billeder og filer skal være i samme mappe eller relative stier (✓ ser ud til at være korrekt)
✅ Repository skal være public (eller du skal have GitHub Pro)

### 6. Fejlfinding
Hvis siden stadig ikke virker:
- Tjek at alle filer er pushet til GitHub (se "Code" fanen)
- Tjek GitHub Pages logs under Settings → Pages → "Visit site" eller "View deployment"
- Vent op til 10 minutter efter første deployment
- Tjek at `index.html` er i roden, ikke i en undermappe

### 7. Opdateringer
Når du laver ændringer:
```powershell
git add .
git commit -m "Beskrivelse af ændringer"
git push
```
GitHub Pages opdateres automatisk efter nogle minutter.

