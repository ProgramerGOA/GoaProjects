* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

header {
    width: 100;
    height: 90;
    background-color: rgb(39, 34, 34);
    color: ;

    display: flex;
    justify-content: space-evenly;
    align-items: center;

    position: fixed;
}

h1 {
    font-size: 45;
}

ul {
    list-style: none;
    display: flex;
    gap: 20;
}

a {
    text-decoration: none;
    color: white;
    font-size: 18;
}

a:hover {
    text-decoration: underline;
}

button {
    padding: 10 20;
    font-size: 18;
    color: white;
    border: 2 solid white;
    background-color: transparent;
}

button:hover {
    background-color: white;
    color: rgb(39, 34, 34);
}

section {
    width: 300;
    height: 300;
    background-color: green;
    border: 5 solid purple;
}

main {
    padding-top: 90;
}