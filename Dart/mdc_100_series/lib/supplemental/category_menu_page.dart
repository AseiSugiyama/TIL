import 'package:flutter/material.dart';
import 'package:meta/meta.dart';

import 'package:Shrine/colors.dart';
import '../model/product.dart';

class CategoryMenuPage extends StatelessWidget {
  final Category currentCategory;
  final ValueChanged<Category> onCategoryTap;
  final List<Category> _categories = Category.values;

  const CategoryMenuPage({
    Key key,
    @required this.currentCategory,
    this.onCategoryTap,
  }) : assert(currentCategory != null);

  Widget __buildCategory(Category category, BuildContext context) {
    var categoryString =
        category.toString().replaceAll('Category.', '').toUpperCase();
    return GestureDetector(
        onTap: () => onCategoryTap(category),
        child: category == currentCategory
            ? Column(
                children: <Widget>[
                  SizedBox(height: 16.0),
                  Text(
                    categoryString,
                    style: Theme.of(context).textTheme.body2,
                    textAlign: TextAlign.center,
                  ),
                  SizedBox(height: 14.0),
                  Container(
                    width: 70.0,
                    height: 2.0,
                    color: Color(0xFFEAA4A4),
                  ),
                ],
              )
            : Container(
                padding: EdgeInsets.symmetric(vertical: 16.0),
                child: Text(
                  categoryString,
                  style: Theme.of(context).textTheme.body2.copyWith(
                        color: kShrineBrown900.withAlpha(153),
                      ),
                  textAlign: TextAlign.center,
                ),
              ));
  }

  @override
  Widget build(BuildContext context) {
    var menuItems = <Widget>[];
    _categories.forEach((Category c) {
      menuItems.add(__buildCategory(c, context));
    });

    return Center(
      child: Container(
        padding: EdgeInsets.only(top: 40.0),
        color: kShrinePink100,
        child: ListView(children: menuItems),
      ),
    );
  }
}
