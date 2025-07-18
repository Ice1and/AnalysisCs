import express from 'express'
import cors from 'cors'
import { MongoClient } from 'mongodb'

const app = express();
app.use(cors());

const URI = 'mongodb://localhost:27017';
const mongoClient = new MongoClient(URI);
await mongoClient.connect();
const database = mongoClient.db('analysisCs')

const getInventory = async (req, res) => {
    try {
        const collection = await database.collection('inventories');
        const result = await collection.find({}).toArray();

        // console.log(result);

        result.forEach(element => {
            element['market_price']['currency'] = 'CNY';
            element['market_price']['numeric_price'] = String(element['market_price']['lowest_price']).replace('¥ ', '') * 1;
            element['buy_price'] = 0;
        })

        res.status(200).json(result);
    } catch (err) {
        console.log(err)
    }
}

const getOverview = async (req, res) => {
    try {
        const collection = await database.collection('inventories');

        // 找到最大的 batch_id
        const cursor = await collection.find().sort({ batch_id: -1 }).limit(1);
        const maxBatchDoc = await cursor.next();
        const maxBatchId = maxBatchDoc.batch_id;
        // 获取所有 batch_id 等于 maximumBatchId 的集合，计算总的 lowest_price 价值并赋值给 numeric_price
        const result = await collection.aggregate([
            { $match: { batch_id: maxBatchId } },
            {
                $addFields: {
                    numeric_price: {
                        $toDouble: {
                            $trim: {
                                input: { $replaceAll: { input: '$market_price.lowest_price', find: '¥', replacement: ''} }
                            }
                        }
                    }
                }
            },

            { $group: { _id: null, total_lowest_price: { $sum: '$numeric_price' }, count: { $sum: 1 } } }
        ]).toArray();

        res.status(200).json(result[0]);
    } catch (err) {
        console.log(err);
    }
}

app.get('/api/v1/getInventory', getInventory);
app.get('/api/v1/getOverview', getOverview);

const port = 3000
app.listen(port, () => {
    console.log(`Server running on port ${port}!`)
})