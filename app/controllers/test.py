from app import responses, cur_query

def cekcek():
    try:
        query = 'select * from public.user'
        cur_query.execute(query)
        data = cur_query.fetchall()

        return responses.success(data, 'data berhasil di tampilkan')
    except Exception as e:
        print(e)