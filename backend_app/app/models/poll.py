def poll_database(db, table, time):
    predictions = table.query.filter(
        db.func.date(table.created_at) == time
    ).all()

    if not predictions:
        most_recent_date = db.session.query(
            db.func.date(table.created_at)
        ).order_by(db.func.date(table.created_at).desc()).first()

        if most_recent_date:
            predictions = table.query.filter(
                db.func.date(table.created_at) == most_recent_date[0]
            ).all()
    response_data = {}

    for match in predictions:
        if match.league not in response_data:
            response_data[match.league] = []
        response_data[match.league].append(match.to_dict())

    return response_data