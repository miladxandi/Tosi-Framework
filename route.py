routes = {
    '/':
        {
            "controller": "home.index",
            "accepted_method": "GET,POST"
        },
    '/user':
        {
            "controller": "user.index",
            "accepted_method": "GET"
        },
    '/user/create':
        {
            "controller": "user.create",
            "accepted_method": "POST"
        }
}
