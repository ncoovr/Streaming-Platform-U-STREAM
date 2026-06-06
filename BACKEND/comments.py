import random
from sqlmodel import Session, select
from db import engine
from models import Videos, Comments

COMENTARIOS_DATA = {
    "Reggaeton": [
        "Un perreo intenso para el fin de semana.", "El ritmo está pegajoso a más no poder.", "Puro fuego en la pista.",
        "Esto va directo a la playlist de la disco.", "El dembow me vuelve loco.", "Rompiendo tarima con este tema.",
        "Flow violento y sin frenos.", "Nadie hace reggaetón como antes, pero esto se acerca.", 
        "Clásico instantáneo para la fiesta.", "A romper la cintura con esto.", "Qué buen beat, no puedo dejar de moverme.",
        "Para bailarlo hasta abajo.", "La verdadera esencia del género.", 
        "El bajo está en su punto perfecto.", "Esto es un hit mundial seguro.", "El fronteo está en otro nivel.",
        "Me transporta a los tiempos dorados del reggaetón.", "Producción impecable.", 
        "Las vocales suenan increíbles.", "De aquí a la cima de las listas."
    ],
    "Trap": [
        "El bajo rompe los audífonos.", "Este trap está durísimo.", "Flow pesado, me encanta.",
        "La nueva escuela viene fuerte.", "Directo a mis favoritos.", "Skrt skrt, qué nivel.",
        "El beat está fuera de este mundo.", "Ese autotune está muy bien usado.", "Trap del real, sin filtros.",
        "Las visuales combinan perfecto con el tema.", "Ese bajo me va a explotar el carro.", "Pura grasa en este track.",
        "El artista tiene un estilo muy marcado.", "Haciendo historia con este sonido.", "Imposible no cabecear con esto.",
        "Nivel internacional, nada que envidiar.", "El ritmo te atrapa desde el segundo uno.", 
        "Este es el hit del verano.", "Producción de primer nivel.", "Fuego puro en esta pista."
    ],
    "Trap Argentino": [
        "Qué locura, rompieron todo boludo.", "Modo diablo activado.", "Argentina en la casa, papá.",
        "El quinto escalón vive en estas rimas.", "Orgullo nacional, puro talento.", "Las barras que tira son una locura.",
        "Se juntaron los que saben.", "Siempre llevando la bandera a lo más alto.", "Esto es historia de la música urbana.",
        "El flow que manejan es de otro planeta.", "No fallan una, qué grandes.", "Directo desde el barrio para el mundo.",
        "El acento le da un toque único.", "Me pone los pelos de punta esta base.", "La escena argentina está imparable.",
        "Otra coronación de gloria.", "Qué junte histórico, por favor.", "Lo mejor que salió esta semana.",
        "Escuchando esto tomando unos mates.", "Simplemente épico."
    ],
    "Alternativa": [
        "Qué propuesta tan interesante y fresca.", "Sonidos que te transportan a otro lugar.", "Una vibra muy distinta a lo habitual.",
        "Me encanta esta mezcla de géneros.", "Arte en su máxima expresión.", "No se parece a nada de lo que escucho normalmente.",
        "Letra profunda y música envolvente.", "El trabajo experimental aquí es genial.", "Una atmósfera sonora increíble.",
        "Es un viaje escuchar este tema.", "La instrumentación es preciosa.", "Para cerrar los ojos y dejarse llevar.",
        "Totalmente fuera de la caja, me fascina.", "Voces etéreas y sintetizadores perfectos.", "Hacía falta algo tan original.",
        "Innovando y rompiendo esquemas.", "El diseño sonoro es magistral.", "Una joya oculta que merece ser descubierta.",
        "Música que te hace sentir cosas.", "Definitivamente va para mis temas de relajación."
    ]
}

def seed_comments():
    with Session(engine) as session:
        videos = session.exec(select(Videos)).all()
        
        if not videos:
            print("No se encontraron videos en la tabla. Verifica que db.sqlite3 tenga datos.")
            return

        for video in videos:
            viejos = session.exec(select(Comments).where(Comments.video_id == video.id)).all()
            for v in viejos:
                session.delete(v)
            
            textos = COMENTARIOS_DATA.get(video.categoria, ["Excelente video"])
            seleccionados = random.sample(textos, min(5, len(textos)))
            
            for texto in seleccionados:
                comentario = Comments(texto=texto, video_id=video.id)
                session.add(comentario)
            
            print(f"Comentarios insertados para: {video.titulo}")
        
        session.commit()
        print("Carga finalizada con exito.")

if __name__ == "__main__":
    seed_comments()