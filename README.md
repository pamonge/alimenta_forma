# 🍽️ Alimenta Forma

**Alimenta Forma** es una aplicación web moderna que combina un backend robusto en **Django** con un frontend rápido y elegante construido en **React** + **Vite**.  
Ideal para gestionar cursos, membresías y perfiles de usuario de manera eficiente y atractiva.

---

## 🚀 Tecnologías Utilizadas

| Backend                  | Frontend                      | Herramientas Adicionales       |
|--------------------------|-------------------------------|-------------------------------|
| 🐍 Python 3.x            | ⚛️ React 18+                   | 🛠️ ESLint (calidad de código)  |
| 🕸️ Django 4.x             | ⚡ Vite (bundler + servidor)  | 🎨 CSS Modules (estilos scoped) |
| 🧩 Django REST Framework | React Router (gestión rutas)  | 📦 npm (gestión frontend)       |

---

## 🗂️ Estructura del Proyecto

```plaintext
/
├── api/                       # Backend Django
│   └── apialimentaforma/
│       ├── api/               # App Django (modelos, vistas, migraciones...)
│       ├── apialimentaforma/  # Configuración general (settings, urls, wsgi)
│       └── manage.py          # Script de gestión Django
├── src/                       # Frontend React
│   ├── components/            # Componentes reutilizables (botones, tarjetas, formularios)
│   ├── routes/                # Páginas principales (Home, Login, Courses, etc.)
│   ├── assets/                # Imágenes y recursos estáticos
│   ├── App.jsx                # Componente raíz React
│   ├── main.jsx               # Punto de entrada React + Vite
│   └── estilos CSS y módulos  # CSS global y módulos CSS
├── index.html                 # Entrada HTML para Vite
├── package.json               # Dependencias frontend
├── requirements.txt           # Dependencias backend
├── vite.config.js             # Configuración de Vite
├── .eslintrc.cjs             # Configuración ESLint
└── .gitignore                 # Archivos ignorados por Git
