from models.note_models import Note, Archive, Tag

NOTES = Note.objects
ARCHIVE = Archive.objects


def add_note(text):
    counter = 0
    if not Note.objects and Archive.objects:
        for a in Archive.objects:
            if counter < a.id_count:
                counter = a.id_count
    if not Archive.objects and Note.objects:
        for n in Note.objects:
            if counter < n.id_count:
                counter = n.id_count
    if Archive.objects and Note.objects:
        for a in Archive.objects:
            for n in Note.objects:
                if a.id_count > n.id_count:
                    counter = a.id_count
                else:
                    counter = n.id_count
    if not Note.objects and not Archive.objects:
        counter = 0
    note = Note(id_count=counter + 1,
                text=text)
    note.save()


def change_note(id_, text):
    for note in NOTES:
        if note.id_count == id_:
            note.update(text=text)
            print(f'Successful change note with id: {id_}')


def del_note(id_):
    for note in NOTES:
        if note.id_count == id_:
            note.delete()
            print(f'Successful delete note with id: {id_}')


def add_date(id_, date):
    for note in NOTES:
        if note.id_count == id_:
            note.update(created=date)
            print(f'Successful add date to note with id: {id_}')


def show_all():
    return NOTES


def done_note(id_):
    notes = Note.objects
    for note in notes:
        if note.id_count == id_:
            arch = Archive(id_count=note.id_count, text=note.text, tags=note.tags)
            arch.save()
            note.delete()


def show_archive():
    return ARCHIVE


def find_note(text):
    som_st = ' '.join(text)
    for n in NOTES:
        created = n.created.strftime("%Y-%m-%d %H:%M:%S")
        if som_st in n.text or som_st in created:
            print(f'Note: {n.id_count}, text: {n.text}, created: {n.created}')


def return_note(id_):
    for a in ARCHIVE:
        if a.id_count == id_:
            note = Note(id_count=a.id_count,
                        text=a.text,
                        tags=a.tags)
            note.save()
            a.delete()
            print(f'Successful return note with id: {id_}')


def add_tag(id_, tags):
    list_tags = []
    [list_tags.append(i) for i in tags]
    for n in Note.objects:
        if n.id_count == id_:
            tag = Tag(id_count=id_, tags=list_tags)
            tag.save()
            note = Note(id_count=id_,
                        text=n.text,
                        tags=tag)
            note.save()
            n.delete()


def clear_all():
    notes = Note.objects
    for n in notes:
        n.delete()


def find_tag(tag):
    str_tag = ' '.join(tag)
    print(str_tag)
    for n in NOTES:
        print('1')
        for i in n.tags.tags:
            print(i)
            if str_tag.lower() in i.lower():
                print(f'Note id: {n.id_count}, date: {n.created.date()}, done: {n.done}\n'
                      f'Text: {n.text}\n'
                      f'Tags: {n.tags.tags}\n'
                      f'---------------------------------------------------------\n')


def show_date(date1, date2):
    for n in NOTES:
        print(n.created)
        if date1.value <= n.created <= date2.value:
            print(f'Id: {n.id_count}, date: {n.created.date()}')
        else:
            print(f'Not find notes with this date')
