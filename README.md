# Tattoo Gallery Project

This is a web project developed in Django that allows displaying a gallery of tattoos and tattoo artists. The project includes functionalities to showcase tattoos, artists, and a customized gallery.

## Requirements

- Python 3.13.1
- Django
- Pillow (for image handling)
- Other packages listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AndreySuavita/Tattoos.git
cd tattoo_project
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
tattoo_project/
├── tattoo_project/          # Main project configuration
├── tattoos/                 # Main tattoos application
│   ├── models.py           # Data models
│   ├── views.py            # Application views
│   ├── urls.py             # URL configuration
│   └── templates/          # HTML templates
├── home/                   # Home page application
├── static/                 # Static files (CSS, JS, etc.)
├── media/                  # Media files (uploaded images)
└── manage.py              # Django management script
```

## Main Routes

- Home page: `/home/`
- Admin panel: `/admin/`
- Gallery: `/tattoos/gallery/`
- Artists list: `/ListArtist/`
- Artist gallery: `/Artist_Gallery/<id>/`

## Models

### TattooArtist
- `name`: Artist name (unique)
- `photo`: Artist photo
- `bio`: Artist biography

### Tattoo
- `title`: Tattoo title
- `image`: Tattoo image
- `artist`: Relationship with the artist (optional)

## Main Views

1. **Gallery**: Displays a gallery of all tattoos in random order
2. **ListArtist**: Shows a list of all artists
3. **Artist_GalleryView**: Displays a specific artist's gallery

## Features

- Randomly ordered tattoo gallery
- Tattoo artist listing
- Individual artist galleries
- Customizable background system
- Customizable logo
- Django admin panel

## Usage

1. Access the admin panel at `/admin` to:
   - Manage artists
   - Upload tattoos
   - Configure backgrounds and logos

2. Navigate through the main gallery to view all tattoos
3. Explore the artist list to see their specific works




