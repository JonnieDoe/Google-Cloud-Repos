'use strict';

const path = require('path');
const nodeModulesPath = path.resolve(__dirname, 'node_modules');
const webpack = require('webpack');
const modulesPath = "absolute_path/app_name/dev_tools"
const appPath = "absolute_path/app_name/main/React"

const config = {
    entry: appPath + '/app/app.js',
    // output config
    output: {
        path: appPath + '/dist/',
        filename: 'bundle.js'
    },
    resolveLoader: {
        modulesDirectories: [
            modulesPath + '/node_modules'
        ]
    },
        resolve: {
        //Resolve module import PATH as app is in different directory than <node_modules>
        root: path.resolve(modulesPath + '/node_modules'),
        extensions: ['', '.js', '.jsx'],
    },
    devtool: 'source-map',
    plugins: [
        // Minify the bundle
    //    new webpack.optimize.UglifyJsPlugin({
    //        compress: {
                // suppresses warnings, usually from module minification
    //        warnings: true,
    //        },
    //    })

    // Allows error warnings but does not stop compiling.
    new webpack.NoErrorsPlugin(),
    ],
    module: {
        loaders: [
          {
            // All .js/.jsx files
            test: [/\.jsx?$/, /\.js?$/],
            // react-hot is like browser sync and babel loads jsx and es6-7
            loader: ['babel'],
            exclude: [nodeModulesPath],
            query: {
              presets: [
                'babel-preset-es2015',
                'babel-preset-react',
              ].map(require.resolve),
            }
          }
        ]
    },
};

module.exports = config;
