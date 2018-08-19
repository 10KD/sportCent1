const User = require('../models').User;
const ncentSDK = require('../../../../../SDK/source/');
const ncentSdkInstance = new ncentSDK();

module.exports = {
    // create(req, res) {
    //     console.log(req.body);
    //     res.status(200).send({ message: req.body });
    // },
    create(req, res) {
        return User
            .create({
                username: req.body.username,
            })
            .then(user => {
                return new Promise(function (resolve, reject) {
                    ncentSdkInstance.createWalletAddress();
                })
                    .then(res.status.send(200))
                    .catch(error => console.log(error));
            })
            .catch(error => {
                console.log(error);
            });
    },

    list(req, res) {
        return User
            .findAll({
                include: [{
                    model: User,
                }],
            })
            .then(user => res.status(200).send(user))
            .catch(error => res.status(400).send(error));
    },
    retrieve(req, res) {
        return User
            .findById(req.params.user_uuid, {
                include: [{
                    model: User,
                }],
            })
            .then(user => {
                if (!user) {
                    return res.status(404).send({
                        message: 'User Not Found',
                    });
                }
                return res.send(user);
            })
            .catch(error => res.status(400).send(error));
    },
};