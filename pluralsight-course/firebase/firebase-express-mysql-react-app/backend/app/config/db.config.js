module.exports = {
    HOST: "localhost",
    USER: "tandoan",
    PASSWORD: "_TanDoan@2023",
    DB: "planning",
    dialect: "mysql",
    pool: {
        max: 5,
        min: 0,
        acquire: 30000,
        idle: 10000
    }
};