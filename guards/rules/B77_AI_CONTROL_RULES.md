# B77 AI-Agent Control Rules

Источник: PROJECT AI CONTROL — UNIVERSAL CORE v1.7.9.2.

## Mandatory before patch
- PRE-CHECK: определить рабочий эталон, границы изменения и критические зависимости.
- Создать физический backup/SHA и SNAPSHOT до изменения рабочего артефакта.
- Для UI — полный UI contour и UI regression corpus.
- Не создавать параллельный механизм, если существует рабочий hook/path.
- Новые функции подключать через существующие hooks.

## Mandatory during patch
- Минимальный патч: один change → проверка → следующий change.
- Проверять event → handler → state → render → model/DB → result.
- Фиксировать существенные события, ошибки, регрессии и решения в журнале проекта.
- Любое структурное изменение вне заявленной области = STOP.

## Mandatory after patch
- Reverse-diff PRE vs POST.
- Added-symbols audit.
- Проверка удаления/добавления/изменения функций относительно заявленной области.
- Полный регрессионный прогон критических путей.
- Для UI: BEFORE_EVIDENCE → CHANGE → AFTER_EVIDENCE → COMPARISON.
- Неподтверждённые артефакты не становятся рабочим эталоном.

## Git policy
- Каждый аудит — отдельный commit с понятным сообщением и отчётом в reports/.
- Аудит получает тег вида audit-vX.Y.Z.
- Исправления — отдельная patch/... ветка.
- Исправления попадают в main через Pull Request.
- Рабочий эталон не заменяется непроверенным кандидатом.
