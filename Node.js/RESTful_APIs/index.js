const express = require('express')
const app = express();
const PORT = 8080;
const cors = require('cors');

app.use(cors())
app.use(express.json())

 

app.listen(
    PORT, () => console.log(`ITS ALIVE!!! on http://localhost:${PORT}` )
)
// conditional 

app.get('/calculate',function(req,res){
	res.send("Example GET");
});
 
app.get('/tshirt', (req, res,) => {
    res.status(200).send
    (
        {
        tshirt: '👕 Weekend Shirt',
        size:'large'
        }
    )
})

// creating new data on the server id is ROUTE PARAMS
app.post('/tshirt/:id', (req,res , stock) => {
    const {id} = req.params;
    const {logo} = req.body;

    if (!logo) {
        res.status(404).send({message: 'Please provide a logo'})
    }

    res.send ({
        tshirt: `👕 with your ${logo} and ID of ${id}`,
    });
})


