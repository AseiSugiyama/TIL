#! /usr/bin/env bash

pkill swift
cd .build/release
./ToDoServer
cd -
