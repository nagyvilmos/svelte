<script>
    import Chart from "../../components/Chart.svelte"

    let content= {
        border: 1,
        items: [
            {
                color: "blue",
                width: 1,
                line: [...Array(101).keys()].map(x => [x,100-((x**2)/100)])
            },
            {
                color: "red",
                width: 3,
                line: [...Array(101).keys()].map(x => [x,((x**2)/100)])
            },
            {
                color: "green",
                width: 4,
                line: [...Array(101).keys()].map(x => [x,100-(((100-x)**2)/100)])
            },
            {
                color: "yellow",
                width: 5,
                rectangle: [20,20,40,40]
            }
        ]
    }
</script>

<h1>Blog</h1>

<Chart width=400 height=400 content={content}/>